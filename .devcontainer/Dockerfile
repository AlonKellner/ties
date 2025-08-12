FROM mcr.microsoft.com/devcontainers/base:debian AS default
COPY ./.devcontainer/install-go.sh ./.devcontainer/migrate_claude.exp dev-pyproject/ ./
ENV GOPATH=/home/vscode/go
ENV PATH="/home/vscode/.local/bin/:/home/vscode/.local/go/bin/:/home/vscode/.cargo/bin:/github/home/.local/bin:/github/home/.local/go/bin:/github/home/.cargo/bin:$GOPATH/bin:$PATH"
ENV NODE_VERSION=24.5.0
ENV NVM_DIR="/home/vscode/.nvm"

USER root
RUN --mount=type=cache,dst=/root/.cache/ --mount=type=cache,dst=/home/vscode/.cache/ DEBIAN_FRONTEND=noninteractive \
    mkdir -p /home/vscode/.cache && chown -R vscode:vscode /home/vscode/.cache && \
    echo apt-tools && apt-get update && apt-get upgrade -y --no-install-recommends && \
    apt-get install -y --no-install-recommends apt-transport-https \
    ca-certificates gnupg curl pkg-config cmake libssl-dev git expect

RUN mkdir -p /home/vscode/.cache && chown -R vscode:vscode /home/vscode/.cache


USER vscode
RUN --mount=type=cache,dst=/home/vscode/.cache/ DEBIAN_FRONTEND=noninteractive \
    echo uv && curl -LsSf https://astral.sh/uv/install.sh | sh && \
    chmod +x $HOME/.local/bin/uv $HOME/.local/bin/uvx && uv self update && uvx --version && \
    echo trivy && curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b $HOME/.local/bin v0.65.0 && \
    chmod +x $HOME/.local/bin/trivy && trivy --version && \
    echo taplo && curl -fsSL https://github.com/tamasfe/taplo/releases/latest/download/taplo-linux-$(uname -m).gz \
    | gzip -d - | install -m 755 /dev/stdin $HOME/.local/bin/taplo && taplo --version && \
    echo go && ./install-go.sh && go version && \
    echo rust && curl -sSf 'https://sh.rustup.rs' | sh -s -- -y && cargo --version && \
    go install github.com/isaacphi/mcp-language-server@latest && mcp-language-server --help && \
    cargo install lychee && lychee --version && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    echo nvm && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && [ -s "$NVM_DIR/bash_completion" ] && \. && nvm --version && \
    echo npm && nvm install ${NODE_VERSION} && node --version && npm --version && \
    echo nodejs && npm install -g npm@latest && node -v && npm -v && \
    echo claude && npm install -g @anthropic-ai/claude-code && claude --version && \
    echo pyright && npm install -g pyright && pyright --version && \
    echo repomix && npm install -g repomix && repomix --version && \
    expect migrate_claude.exp
