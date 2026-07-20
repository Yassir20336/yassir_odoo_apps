from odoo import fields, models, _


class ProductProduct(models.Model):
    _inherit = "product.product"

    total_qty_all_companies = fields.Float(
        string="Total Qty (All Companies)",
        compute="_compute_total_qty_all_companies",
        compute_sudo=True,
        digits="Product Unit of Measure",
    )

    location_qty_details = fields.Html(
        string=" ",
        compute="_compute_location_qty_details",
        compute_sudo=True,
        sanitize=False,
    )

    def _compute_total_qty_all_companies(self):
        quant_obj = self.env["stock.quant"].sudo()

        for product in self:
            quants = quant_obj.search([
                ("product_id", "=", product.id),
                ("location_id.usage", "=", "internal"),
            ])
            product.total_qty_all_companies = sum(quants.mapped("quantity"))

    def _compute_location_qty_details(self):
        for product in self:
            product.location_qty_details = self._build_location_qty_details([product.id])

    def _build_location_qty_details(self, product_ids):
        if not product_ids:
            return f"<p>{_('No stock available.')}</p>"

        if isinstance(product_ids, int):
            product_ids = [product_ids]

        quant_obj = self.env["stock.quant"].sudo()

        quants = quant_obj.search([
            ("product_id", "in", product_ids),
            ("location_id.usage", "=", "internal"),
        ])

        if not quants:
            return f"<p>{_('No stock available.')}</p>"

        grouped = {}

        for quant in quants:
            key = (
                quant.company_id.name,
                quant.location_id.display_name,
            )

            if key not in grouped:
                grouped[key] = {
                    "quantity": 0.0,
                    "available": 0.0,
                }

            grouped[key]["quantity"] += quant.quantity
            grouped[key]["available"] += quant.available_quantity

        total_qty = 0.0
        total_available = 0.0

        html = f"""
        <table class="table table-sm table-bordered table-hover"
               style="width:100%; text-align:center;">
            <thead style="background:#f8f9fa;">
                <tr>
                    <th>{_("Company")}</th>
                    <th>{_("Location")}</th>
                    <th>{_("On Hand")}</th>
                    <th>{_("Available")}</th>
                </tr>
            </thead>
            <tbody>
        """

        for (company, location), values in sorted(grouped.items()):
            total_qty += values["quantity"]
            total_available += values["available"]

            html += f"""
                <tr>
                    <td>{company}</td>
                    <td>{location}</td>
                    <td><strong>{values['quantity']:,.2f}</strong></td>
                    <td><strong>{values['available']:,.2f}</strong></td>
                </tr>
            """

        html += f"""
            </tbody>
            <tfoot>
                <tr style="background:#f8f9fa;font-weight:bold;">
                    <td colspan="2">{_("Total")}</td>
                    <td>{total_qty:,.2f}</td>
                    <td>{total_available:,.2f}</td>
                </tr>
            </tfoot>
        </table>
        """

        return html


class ProductTemplate(models.Model):
    _inherit = "product.template"

    total_qty_all_companies = fields.Float(
        string="Total Qty (All Companies)",
        compute="_compute_total_qty_all_companies",
        compute_sudo=True,
        digits="Product Unit of Measure",
    )

    location_qty_details = fields.Html(
        string=" ",
        compute="_compute_location_qty_details",
        compute_sudo=True,
        sanitize=False,
    )

    def _compute_total_qty_all_companies(self):
        for template in self:
            template.total_qty_all_companies = sum(
                template.product_variant_ids.mapped("total_qty_all_companies")
            )

    def _compute_location_qty_details(self):
        for template in self:
            template.location_qty_details = (
                self.env["product.product"]
                .browse([])
                ._build_location_qty_details(template.product_variant_ids.ids)
            )