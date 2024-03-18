import { Component } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { PatientService } from '../services/patient/patient.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent {
  form!: FormGroup;

  constructor(private formBuilder: FormBuilder,private patientService:PatientService,private router:Router) {}

  
  
  ngOnInit(): void {
  
  this.form = this.formBuilder.group( {
  
    age:'',

    sex:'',

    blood_group:'',

    weight:'',

    height:'',

    bmi:''
  
  
  });
  
  }


  submit() {
    this.patientService.register(this.form.getRawValue()).subscribe(
      (res)=>console.log(res)
    )
    this.router.navigate(['/pboard']);
  }


  // if the form is already filled don't need to fill it again

  Done()
  {
    this.router.navigate(['/pboard']);
  }

  
}
