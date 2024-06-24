import { DoctorService } from '../../../../architecture/services/doctor/doctor.service';
import { Component, OnInit } from '@angular/core';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';
import { EChartsOption } from 'echarts';

@Component({
  selector: 'app-doc',
  templateUrl: './doc.component.html',
  styleUrls: ['./doc.component.css']
})
export class DocComponent implements OnInit{
  doctorData: any = {};
  totalAppointments: number = 0;
  uniquePatientCount: number = 0;

  
  constructor(private doctorService: DoctorService) {
    this.updateChartData();
  }
  
  ngOnInit(): void {
    this.doctorService.getDoctor().subscribe((res: any) => {
      this.doctorData = res;
      // console.log("coming from dashboard", this.doctorData);
    });
  
    this.doctorService.getbookedAppointments().subscribe((appointments: any) => {
      this.totalAppointments = appointments.length;
      this.uniquePatientCount = [...new Set(appointments.map((a:any) => a.patient))].length;
      this.updateChartData();
    });


   
  }

  updateChartData() {
    if (this.option.series && Array.isArray(this.option.series) && this.option.series.length > 0) {
      this.option.series[0].data = [
        { value: this.totalAppointments, name: 'Total Appointments' },
        { value: this.uniquePatientCount, name: 'Unique Patients' },
        // Add more data points as needed
      ];
    }
  }


  option:EChartsOption ={
    tooltip: {
      trigger: 'item'
    },
    legend: {
      top: '5%',
      left: 'center'
    },
    series: [
      {
        name: 'Access From',
        type: 'pie',
        radius: ['40%', '70%'],
        avoidLabelOverlap: false,
        padAngle: 5,
        itemStyle: {
          borderRadius: 10,
        },
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 40,
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
        data: [
          { value: 1048, name: 'Search Engine' },
          { value: 735, name: 'Direct' },
          { value: 580, name: 'Email' },
          { value: 484, name: 'Union Ads' },
          { value: this.uniquePatientCount, name: 'Total Patients' }
        ]
      }
    ]
  };
}
