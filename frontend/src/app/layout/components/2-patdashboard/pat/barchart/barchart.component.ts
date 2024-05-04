import { Component } from '@angular/core';
import { EChartsOption } from 'echarts';

@Component({
  selector: 'app-barchart',
  templateUrl: './barchart.component.html',
  styleUrls: ['./barchart.component.css']
})
export class BarchartComponent {
  option:EChartsOption = {

    color: [
      '#c23531',
      '#2f4554',
      
    ],

    title: {
      text: 'Recovery Rate'
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow',
        
      },
      formatter: '{b}: {c}%'
    },
    legend: {},
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      boundaryGap: [0, 0.001],
      
    },
    yAxis: {
      type: 'category',
      data: ['Cold', 'Fracture', 'Acne', 'Hematoma', 'Caries']
    },
   
    series: [
      
      {
        name: '2011',
        type: 'bar',

        data: [10, 20, 30, 40, 50, 60], // Provide numerical values,
        itemStyle: {
          color: function(params) {
            var colorList = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#91c7ae'];
            return colorList[params.dataIndex];
          }
        }
      
      },
      {
        name: '2012',
        type: 'bar',

        data: [70, 80, 90, 100, 110, 120], // Provide numerical values
        itemStyle: {
          color: function(params) {
            var colorList = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#91c7ae'];
            return colorList[params.dataIndex];
          }
        }
      }
    ]
  };
  
}
