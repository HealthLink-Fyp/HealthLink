import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { NotifyService } from '../../notification/notify.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  form: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router,
    private notifyService: NotifyService
  ) {
    this.form = this.createForm();
  }

  private createForm(): FormGroup {
    return this.formBuilder.group({
      email: '',
      password: ''
    });
  }

  submit(): void {
    this.authService.login(this.form.getRawValue()).subscribe(
      (res: any) => {
        if (res.access_token) {
          this.authService.accessToken = res.access_token;
          this.notifyService.showSuccess("Logged in successfully!");
          AuthService.authEmitter.emit(true);
          this.router.navigate(['/auth']);
          localStorage.setItem('token', res.access_token);
        } else {
          this.notifyService.showError('Wrong Credentials! Try again');
        }
      },
      error => {
        console.error('Error:', error);
        this.notifyService.showError('Wrong Credentials! Try again');
      }
    );
  }
}




// Scalability & Maintainability:

// Form created in constructor via createForm().
// Unused OnInit interface removed.
// Simplified login logic.
// Alternative:

// Streamlined notification logic.
// Resource Utilization:

// Unused imports removed.
// Faster Processing:

// Optimized navigation post-authentication.