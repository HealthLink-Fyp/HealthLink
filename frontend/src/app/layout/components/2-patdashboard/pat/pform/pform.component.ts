import { Component } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';
import { ActivatedRoute, Router } from '@angular/router';
import { NotifyService } from '../../../notification/notify.service';

@Component({
  selector: 'app-pform',
  templateUrl: './pform.component.html',
  styleUrls: ['./pform.component.css']
})

export class PformComponent {
  form!: FormGroup;
  isUpdateMode = false;     //when clicked on update button in dashboard component, it recevies
                            // a true boolean value updatemode=true which in turn sets it to true

  constructor(private formBuilder: FormBuilder,private patientService:PatientService,private route:ActivatedRoute,private router:Router, private notifyService:NotifyService) {}

  
  
  ngOnInit(): void {
    this.route.queryParams.subscribe(params=>{
      this.isUpdateMode=params['updateMode'] ||false;        //catch the boolean value from dashboard compoent
      this.createForm();                                     //create the entire form fields
      if (this.isUpdateMode) {                               //if update is true
        this.getPatientDataFields();                         // fill out the form fields with patient data
      }
    })
   
  
  }

  getPatientDataFields() {
    this.patientService.getPatient().subscribe(data => this.form.patchValue(data));   //re-write the patient data on the form fields
  }

  createForm()
  {
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
    const method = this.isUpdateMode ? 'updatePatientProfile' : 'register';
    this.patientService[method](this.form.getRawValue()).subscribe(
      (res: any) => {
        if(res.user!=null) {
          this.notifyService.showSuccess('Successfully created patient profile!')
          this.router.navigate(['/patient/dashboard']);
        } else {
          this.notifyService.showError('Fill out the whole Form!')
        }
        console.log("response for pform notify service", res);
      },
      error => {
        console.error('Error:', error)
        this.notifyService.showError(' Error! Please fill out the whole Form')
      }
    );
  }

  toggleUpdateMode() {                               //used for cancel button which empties out the form fields and does not update the form
    this.isUpdateMode = !this.isUpdateMode;
    
  }


  // if the form is already filled don't need to fill it again

  Done()
  {
    this.router.navigate(['/patient/dashboard']);
  }

}
