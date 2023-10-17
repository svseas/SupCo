/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
export class ColorTemplate extends Component {
    setup(){
        super.setup(...arguments);
    }

    variants = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900];
    colorNames = [
        "primary-bg-",
        "cerise-red-",
        "golden-bell-",
        "olive-drab-",
        "pacific-blue-",
        "dark-orchid-",
        "dayshift-",
        "nightshift-",
    ];
}
ColorTemplate.template = "mes-bom-ui.color_template";