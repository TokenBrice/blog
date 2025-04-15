FROM hugomods/hugo:0.111.3
#FROM hugomods/hugo:0.125.3

WORKDIR /src

COPY . .

# Install submodules
RUN git config --global --add safe.directory /workspace
RUN git submodule update --init --recursive

RUN hugo --gc --minify