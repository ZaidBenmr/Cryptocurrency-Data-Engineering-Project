import { NgModule } from "@angular/core";
import { HttpClientModule } from "@angular/common/http";
import { RouterModule } from "@angular/router";
import { CommonModule } from "@angular/common";
import { FormsModule } from "@angular/forms";

import { AdminLayoutRoutes } from "./admin-layout.routing";
import { DashboardComponent } from "../../pages/dashboard/dashboard.component";
import { PredictionsComponent } from "../../pages/predictions/predictions.component";
//import { VolatiltyComponent } from '../../pages/volatilty/volatilty.component';
//import { CumreturnsComponent } from "../../pages/cumreturns/cumreturns.component";
//import { CorrelationComponent } from "../../pages/correlation/correlation.component";
//import { CryptobalanceComponent } from "../../pages/cryptobalance/cryptobalance.component";
// import { IconsComponent } from "../../pages/icons/icons.component";
// import { NotificationsComponent } from "../../pages/notifications/notifications.component";
// import { UserComponent } from "../../pages/user/user.component";
// import { TablesComponent } from "../../pages/tables/tables.component";
// import { TypographyComponent } from "../../pages/typography/typography.component";
// import { RtlComponent } from "../../pages/rtl/rtl.component";

import { NgbModule } from "@ng-bootstrap/ng-bootstrap";

import * as PlotlyJS from 'plotly.js/dist/plotly.js';
import { PlotlyModule } from 'angular-plotly.js';
PlotlyModule.plotlyjs = PlotlyJS;

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(AdminLayoutRoutes),
    FormsModule,
    PlotlyModule,
    HttpClientModule,
    NgbModule,
    
  ],
  declarations: [
    DashboardComponent,
    PredictionsComponent
  ]
})
export class AdminLayoutModule {}
