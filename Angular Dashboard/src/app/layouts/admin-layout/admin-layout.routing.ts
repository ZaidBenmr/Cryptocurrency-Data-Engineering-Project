import { Routes } from "@angular/router";

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

export const AdminLayoutRoutes: Routes = [
  { path: "dashboard", component: DashboardComponent },
  { path: "predictions", component: PredictionsComponent },
  //{ path: "volatilty", component: VolatiltyComponent },
  //{ path: "cumreturns", component: CumreturnsComponent },
  //{ path: "correlation", component: CorrelationComponent },
  //{ path: "cryptobalance", component: CryptobalanceComponent },
  // { path: "icons", component: IconsComponent },
  // { path: "notifications", component: NotificationsComponent },
  // { path: "user", component: UserComponent },
  // { path: "tables", component: TablesComponent },
  // { path: "typography", component: TypographyComponent },
  // { path: "rtl", component: RtlComponent }
];
