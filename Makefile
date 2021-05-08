SHELL = /bin/bash
package = shagen/sbom-lint

.PHONY: all available
all:
	@echo "usage: "
	@echo "       make clean - removes output files"
	@echo "       make image - builds container image"
	@echo "       make available - push container image to docker hub"

clean:
	@echo "- removing output files"
	@rm -f *.log

image:
	@echo "- building container image"
	set -e ;\
	RND_SEED=$$(openssl rand -base64 48) ;\
	BUILD_TS=$$(date -u +'%Y-%m-%dT%H:%M:%SZ') ;\
	REVISION=$$(git rev-parse --verify HEAD) ;\
	VERSION=$$(grep version setup.py | cut -f2 -d'"') ;\
	echo $$RND_SEED $$BUILD_TS ;\
	docker buildx use rekcod ;\
	docker buildx inspect rekcod ;\
	docker buildx build \
	--output=type=registry \
	--platform linux/amd64,linux/arm64,linux/arm/v7 \
	--no-cache \
	--build-arg BUILD_TS=$$BUILD_TS \
	--build-arg REVISION=$$REVISION \
	--build-arg VERSION=$$VERSION \
	--tag $(package) . ;\

	@echo "Result: $$(docker inspect -f \
	'version={{index .Config.Labels "org.opencontainers.image.version"}}\
	timestamp={{index .Config.Labels "org.opencontainers.image.created"}}\
	revision=sha1:{{index .Config.Labels "org.opencontainers.image.revision"}}' \
	$(package))" ;\

available:
	@echo "- publishing container image on hub.docker.com"
	@echo " + docker inspect says:"
	@echo "   $$(docker inspect -f \
	'version={{index .Config.Labels "org.opencontainers.image.version"}}\
	timestamp={{index .Config.Labels "org.opencontainers.image.created"}}\
	revision=sha1:{{index .Config.Labels "org.opencontainers.image.revision"}}' \
	$(package))" ;\
	docker push $(package) ;\
