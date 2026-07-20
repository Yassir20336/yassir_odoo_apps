/** @odoo-module **/
document.addEventListener('click', (ev)=>{
 const tr=ev.target.closest('tr.o_data_row');
 if(!tr) return;
 document.querySelectorAll('tr.o_data_row.hcr_selected').forEach(r=>r.classList.remove('hcr_selected'));
 tr.classList.add('hcr_selected');
});
