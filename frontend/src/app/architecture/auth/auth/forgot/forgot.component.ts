import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { ForgotService } from 'src/app/architecture/services/forgot.service';

@Component({
  selector: 'app-forgot',
  templateUrl: './forgot.component.html',
  styleUrls: ['./forgot.component.css'],
})
export class ForgotComponent implements OnInit {
  cls = '';

  message = '';

  form!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private forgotService: ForgotService,
  ) {}

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      email: '',
    });
  }

  submit() {
    this.forgotService.forgot(this.form.getRawValue()).subscribe(
      () => {
        this.cls = 'success';
        this.message = 'Email was sent';
      },
      () => {
        this.cls = 'danger';
        this.message = 'Error occurred!';
      },
    );
  }
}
