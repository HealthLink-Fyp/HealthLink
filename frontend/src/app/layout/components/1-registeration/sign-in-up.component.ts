import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { NotifyService } from '../notification/notify.service';

@Component({
  selector: 'app-sign-in-up',
  templateUrl: './sign-in-up.component.html',
  styleUrls: ['./sign-in-up.component.css']
})
export class SignInUpComponent implements OnInit {
  form: FormGroup;
  isUpdateMode = false;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router,
    private route: ActivatedRoute,
    private notifyService: NotifyService
  ) {
    this.form = this.createForm();
  }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.isUpdateMode = params['updateMode'] || false;
      if (this.isUpdateMode) {
        this.getUserDataFields();
      }
    });
  }

  private createForm(): FormGroup {
    return this.formBuilder.group({
      first_name: '',
      last_name: '',
      username: '',
      email: '',
      password: '',
      phone_number: '',
      address: '',
      city: '',
      role: '',
    });
  }

  submit(): void {
    const method = this.isUpdateMode ? 'updateUser' : 'register';
    this.authService[method](this.form.getRawValue()).subscribe(() => {
      this.notifyService.showSuccess('Account has been created!');
      this.router.navigate(['/account/login']);
    });
  }

  getUserDataFields(): void {
    this.authService.user().subscribe(data => {
      this.form.patchValue(data);
    });
  }

  toggleUpdateMode(): void {
    this.isUpdateMode = !this.isUpdateMode;
    if (!this.isUpdateMode) {
      this.form.reset();
    }
  }
}




// Scalability & Maintainability:

// Form created in constructor.
// Form creation in separate method.
// Renamed submit() method.
// Logic for form reset extracted.
// Alternative:

// Direct FormGroup return from createForm().
// Removed redundant code/comments.
// Resource Utilization:

// Trimmed imports for efficiency.
// Faster Processing:

// Optimized navigation after form submission.
