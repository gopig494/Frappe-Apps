// Copyright (c) 2021, Gopi and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ord', {
	
    timeline_refresh:function(frm){
        if(frm.doc.payment_status =='Paid'){
        	frm.add_custom_button(__('Inprogress'), function(){
        		frm.set_value('order_status','In progress')

        	});
        }
        

	},
	refresh:function(frm){
		if(frm.doc.order_status =='In progress'){
        	frm.add_custom_button(__('Completed'), function(){
        		frm.set_value('order_status','completed')

        	});
        }

	},

// 	refresh:function(frm){
// 		if (frm.doc.docstatus == 1){
			


//             	frm.add_custom_button(__('Make Payment'), function(){

//                		var post_data = {
//                        		"customer_name":cur_frm.doc.customer_name,
//                        		"payment_type":"Pay",
//                        		"payment_mode":"Cash",
//                        		"paid_status":"Paid",
//                             "paid_amount":"300",
//                        		"reference":[{"type":"Ord","namee":cur_frm.doc.name,"total":cur_frm.doc.total_amount}]

//                        	}
        
//         $.ajax({
//             headers: { "X-Frappe-CSRF-Token": frappe.csrf_token },
//             method:'POST',
//             url:'http://192.168.0.156:8000/api/resource/Payment entryb',
//             dataType: 'json',
//             data:JSON.stringify(post_data),
        
//         success:function(data){console.log("sucess insert"+data);},
//         error:function(err){console.log(err);},
//         });


         
//     });
        
        
   
    
// }
// }

	// onload: function(frm) {
	// 	 // Api Post Data
 //            var post_data = {

 //                       "customer_name":"Sam",
 //                       "customer_address":"Sample address",
 //                       "product_details":[{"type":"Productb","name1":"PROD01"}]
                       
 //                         // "docstatus":0 ,
                         
 //                        }
        
 //        $.ajax({
 //            headers: { "X-Frappe-CSRF-Token": frappe.csrf_token },
 //            method:'POST',
 //            url:'http://192.168.0.156:8000/api/resource/Ord',
 //            dataType: 'json',
 //            data:JSON.stringify(post_data),
        
 //        success:function(data){console.log("sucess insert"+data);},
 //        error:function(err){console.log(err);},
 //        });

	// }
});



