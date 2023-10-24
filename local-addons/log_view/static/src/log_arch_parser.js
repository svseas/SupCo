/** @odoo-module */

import { XMLParser } from "@web/core/utils/xml";

export class LogArchParser extends XMLParser {
  parse(arch) {
    const xmlDoc = this.parseXML(arch);
    const letterId = xmlDoc.getAttribute("letter_id");
    return {
      letterId,
    };
  }
}
