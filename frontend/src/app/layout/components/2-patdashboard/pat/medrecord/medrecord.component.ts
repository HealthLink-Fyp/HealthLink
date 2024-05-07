import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-medrecord',
  templateUrl: './medrecord.component.html',
  styleUrls: ['./medrecord.component.css']
})
export class MedrecordComponent {

  selectedFile!: File;

  constructor(private uploadService: PatientService) { }

  ngOnInit(): void {
  }

  uploadFile(event: any) {
    this.selectedFile = event.target.files[0];
  }

  sendFileToBackend() {
    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.uploadService.uploadFile(formData).subscribe((res: any) => {
      console.log('File sent to backend:', res);
    });
  }

}
