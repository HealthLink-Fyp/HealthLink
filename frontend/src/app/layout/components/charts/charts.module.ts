import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ChartsRoutingModule } from './charts-routing.module';
import { ChartsComponent } from './charts.component';
import { BarchartComponent } from './barchart/barchart.component';
import { NgxEchartsModule } from 'ngx-echarts';


@NgModule({
  declarations: [
    ChartsComponent,
    BarchartComponent
  ],
  imports: [
    CommonModule,
    ChartsRoutingModule,
    NgxEchartsModule.forRoot({
      /**
       * This will import all modules from echarts.
       * If you only need custom modules,
       * please refer to [Custom Build] section.
       */
      echarts: () => import('echarts'), // or import('./path-to-my-custom-echarts')
    }),
  ],
exports:[BarchartComponent]
})
export class ChartsModule { }
