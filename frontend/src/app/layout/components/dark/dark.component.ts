import { Component } from '@angular/core';
import { ThemeService } from './theme.service';

@Component({
  selector: 'app-dark',
  templateUrl: './dark.component.html',
  styleUrls: ['./dark.component.css']
})
export class DarkComponent {
  constructor(private themeService: ThemeService) {}

  toggleTheme(checked: boolean) {
    if (checked) {
      this.themeService.enableDarkTheme();
    } else {
      this.themeService.enableLightTheme();
    }
  }
}
