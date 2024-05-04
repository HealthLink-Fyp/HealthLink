import { AuthService } from 'src/app/architecture/services/auth.service';
import { Component, OnInit } from '@angular/core';
import { MaterialModule } from 'src/app/architecture/material/material/material.module';
@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css'],
})
export class NavComponent implements OnInit {
  authenticated = false;

  constructor(private authService: AuthService) {}

  ngOnInit(): void {
    AuthService.authEmitter.subscribe((authenticated) => {
      this.authenticated = authenticated;
    });
  }

  logout() {
    this.authService.logout().subscribe(() => {
      this.authService.accessToken = '';
      AuthService.authEmitter.emit(false);
    });
  }
}
