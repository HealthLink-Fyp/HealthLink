import { Component } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { PatientService } from '../services/patient/patient.service';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css'],
})
export class PatientComponent {
  form!: FormGroup;
  searchTimeout: any = null;

  constructor(
    private formBuilder: FormBuilder,
    private patientService: PatientService
  ) {}

  formSubmitted: boolean = false;
  searchQuery: string = '';
  searchResults: any[] = [];

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      age: '',
      sex: '',
      blood_group: '',
      weight: '',
      height: '',
      bmi: '',
    });
  }

  submit() {
    this.patientService
      .register(this.form.getRawValue())
      .subscribe((res) => console.log(res));
    this.formSubmitted = true;
  }

  getProfilePhotoUrl(url: string): string {
    const currentHost = window.location.origin.replace('4200', '8000');
    return url.replace('http://localhost:8000', currentHost);
  }

  onSearchQueryChange() {
    clearTimeout(this.searchTimeout);
    this.searchTimeout = setTimeout(() => {
      this.searchDoctors();
    }, 500);
  }

  searchDoctors() {
    this.patientService
      .searchDoctors(this.searchQuery)
      .subscribe((response: any) => {
        this.searchResults = response;
      });
  }
}
