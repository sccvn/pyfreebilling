FROM golang:1.19-alpine AS builder

LABEL maintainer="Mathias WOLFF <mathias@celea.org> (https://www.pyfreebilling.com/)"

# Move to working directory (/build).
WORKDIR /build
RUN apk update && \
  apk --no-cache add ca-certificates wget && \
  apk --no-cache add build-base
# Copy and download dependency using go mod.
COPY go.mod go.sum ./
RUN go mod download

# Copy the code into the container.
COPY . ./

# Set necessary environment variables needed for our image and build the API server.
RUN go mod verify
ENV CGO_ENABLED=1 GOOS=linux GOARCH=amd64
#RUN go build -ldflags='-s' -o=./bin/pks-admin ./main.go
RUN go build -ldflags='-linkmode external -extldflags "-static"' -o=./bin/linux_amd64/pks-admin ./main.go

# FROM debian:bookworm-slim
# RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
#     ca-certificates && \
#     rm -rf /var/lib/apt/lists/*
FROM scratch

# Copy binary and config files from /build to root folder of scratch container.
# COPY --from=builder ["/build/bin/linux_amd64/pks-admin", "/build/.env", "/"]
COPY --from=builder /build/bin/linux_amd64/pks-admin /
COPY --from=builder /build/.env /
# Command to run when starting the container.
ENTRYPOINT ["/pks-admin"]
