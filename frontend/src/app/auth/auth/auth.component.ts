import { AuthService } from 'src/app/services/auth.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css'],
})
export class AuthComponent implements OnInit {
  message = '';

  amWho = '';

  constructor(
    private authService: AuthService,
    private router: Router,
  ) {}

  ngOnInit(): void {
    this.authService.user().subscribe({
      next: (res: any) => {
        this.message = `Hi ${res.first_name} ${res.last_name}`;

        this.amWho = res.role;
        if (this.amWho == 'doctor') {
          this.router.navigate(['/doctor/form']);
        } else {
          this.router.navigate(['/patient/form']);
        }
        AuthService.authEmitter.emit(true);
      },
      error: (err) => {
        this.message = 'u r not authenticated';
        AuthService.authEmitter.emit(false);
      },
    });
  }
}
