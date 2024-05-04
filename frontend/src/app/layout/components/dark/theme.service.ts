import { Injectable, Renderer2, RendererFactory2 } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ThemeService {

  private renderer: Renderer2;

  constructor(private rendererFactory: RendererFactory2) {
    this.renderer = this.rendererFactory.createRenderer(null, null);
  }

  enableDarkTheme() {
    this.renderer.addClass(document.body, 'theme-dark');
  }

  enableLightTheme() {
    this.renderer.removeClass(document.body, 'theme-dark');
  }
}
