declare module "ts/gallery" {
    export default class StackGallery {
        constructor(container: HTMLElement);
    }
}

declare module "ts/color" {
    export function getColor(
        key: string | null,
        hash: string | null,
        imageURL: string
    ): Promise<{
        DarkMuted: { rgb: number[] };
        Vibrant: { rgb: number[] };
    }>;
}

declare module "ts/menu" {
    export default function menu(): void;
}

declare module "ts/createElement" {
    export default function createElement(
        tag: string,
        attrs: Record<string, unknown> | null,
        ...children: unknown[]
    ): HTMLElement;
}

declare module "ts/colorScheme" {
    export default class StackColorScheme {
        constructor(toggle: HTMLElement | null);
    }
}

declare module "ts/smoothAnchors" {
    export function setupSmoothAnchors(): void;
}
