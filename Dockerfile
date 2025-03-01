# Fleek
#FROM klakegg/hugo:0.69.0-ext
##FROM hugomods/hugo:0.69
# Working
FROM hugomods/hugo:0.111.3

# Latest
#FROM klakegg/hugo:0.111.3-ext
#FROM hugomods/hugo:latest

# TokenBrice
#FROM klakegg/hugo:0.125.3-ext
#FROM hugomods/hugo:0.125.3

WORKDIR /src

COPY . .

# Install submodules
RUN git config --global --add safe.directory /workspace
RUN git submodule update --init --recursive

RUN hugo --gc --minify