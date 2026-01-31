FROM hugomods/hugo:0.148.2

WORKDIR /src

COPY . .

# Install submodules
RUN git config --global --add safe.directory /workspace
RUN git submodule update --init --recursive

RUN hugo --gc --minify