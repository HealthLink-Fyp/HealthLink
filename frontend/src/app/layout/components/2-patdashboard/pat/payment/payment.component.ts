import { Component, OnInit  } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';


@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.css']
})
export class PaymentComponent implements OnInit {

  constructor(private router:Router,private route:ActivatedRoute){}

  paymentDone:boolean=false;

  ngOnInit(): void {
    this.doctorId=this.route.snapshot.paramMap.get('doctorId');
    console.log("doctor id is coming in payment component",this.doctorId);
  }
  amount = '100.00';

  doctorId:any="";

  paymentRequest: google.payments.api.PaymentDataRequest = {
    apiVersion: 2,
    apiVersionMinor: 0,
    allowedPaymentMethods: [
      {
        type: 'CARD',
        parameters: {
          allowedAuthMethods: ['PAN_ONLY', 'CRYPTOGRAM_3DS'],
          allowedCardNetworks: ['MASTERCARD', 'VISA'],
        },
        tokenizationSpecification: {
          type: 'PAYMENT_GATEWAY',
          parameters: {
            gateway: 'example',
            gatewayMerchantId: 'exampleGatewayMerchantId',
          },
        },
      },
    ],
    merchantInfo: {
      merchantId: '12345678901234567890',
      merchantName: 'Demo Merchant',
    },
    transactionInfo: {
      totalPriceStatus: 'FINAL',
      totalPriceLabel: 'Total',
      totalPrice: this.amount,
      currencyCode: 'PKR',
      countryCode: 'PK',
    },
  };

  onLoadPaymentData = (event: Event): void => {
    if ('detail' in event) {
      const customEvent = event as CustomEvent<google.payments.api.PaymentData>;
      console.log('PaymentData Loaded', customEvent.detail);
    } else {
      console.error('Event does not contain detail property');
    }
  };

  onError = (event: ErrorEvent): void => {
    console.error('error', event.error);
  };



  onPaymentDone()
  {
    console.log(this.doctorId);
    this.router.navigate(['/patient/appointments', this.doctorId]);
  }

  onPaymentDataAuthorized: google.payments.api.PaymentAuthorizedHandler = (
    paymentData
  ) => {
    console.log('Pyament authorized', paymentData);
     this.paymentDone=true;
    return {
      transactionState: 'SUCCESS',
     
    };
   
   
  };
}
