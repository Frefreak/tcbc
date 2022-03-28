jd_rev/sign/lib/libsign.so:
	make -C jd_rev/sign/lib

prepare: jd_rev/sign/lib/libsign.so

image: prepare
	docker build . -t tcbc_backend:v$(shell date "+%Y%m%d") \
		--build-arg http_proxy=${CONTAINER_PROXY} \
		--build-arg https_proxy=${CONTAINER_PROXY} \


dev: prepare
	uvicorn server:app --reload

