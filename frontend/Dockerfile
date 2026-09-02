FROM node:22-bullseye-slim

WORKDIR /app

RUN corepack enable && corepack prepare pnpm@10.32.1 --activate

COPY package.json pnpm-lock.yaml /app/

ENV PUPPETEER_SKIP_DOWNLOAD=true

RUN pnpm install --frozen-lockfile

COPY ./ /app/

EXPOSE 5173

CMD ["pnpm", "dev", "--host", "0.0.0.0"]