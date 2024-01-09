/** @odoo-module */
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class OrmExample extends Component {
  setup() {
    this.orm = useService("orm");
  }

  async loadBom() {
    const bom = await this.orm.searchRead(
      "mrp.bom",
      [],
      ["name", "tech_process_ids", "ng_percent", "created_by", "approved_by", "bom_uom"]
    );

    console.log(bom);
  }
}

OrmExample.template = "mes-bom-ui.orm-example";
