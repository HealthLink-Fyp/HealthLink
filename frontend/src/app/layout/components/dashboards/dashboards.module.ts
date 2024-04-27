import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardsRoutingModule } from './dashboards-routing.module';
import { DashboardsComponent } from './dashboards.component';
import { DocComponent } from './doc/doc.component';
import { PatComponent } from './pat/pat.component';
import { PsidenavComponent } from './pat/psidenav/psidenav.component';
import { PtabsComponent } from './pat/ptabs/ptabs.component';
import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';
import { BarchartComponent } from './charts/barchart/barchart.component';

import { BodychartComponent } from './charts/bodychart/bodychart.component';

import { MaterialModule } from 'src/app/material/material/material.module';

import { NgxEchartsModule } from 'ngx-echarts';


import { PformComponent} from './pat/pform/pform.component';
import { DocsearchComponent } from './pat/docsearch/docsearch.component';
import { DformComponent } from './doc/dform/dform.component';



@NgModule({
  declarations: [
    DashboardsComponent,
    DocComponent,
    PatComponent,
    PsidenavComponent,
    PtabsComponent,
    DsidenavComponent,
    BodychartComponent,
    BarchartComponent,

    
  ],
  imports: [
    CommonModule,
    DashboardsRoutingModule,
    MaterialModule,

    
    NgxEchartsModule.forRoot({
      /**
       * This will import all modules from echarts.
       * If you only need custom modules,
       * please refer to [Custom Build] section.
       */
      echarts: () => import('echarts'), // or import('./path-to-my-custom-echarts')
    }),
  ],
  exports:[PsidenavComponent]
})
export class DashboardsModule { }
