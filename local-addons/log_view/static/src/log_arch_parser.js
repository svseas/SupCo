/** @odoo-module */

import { XMLParser } from "@web/core/utils/xml";

export class LogArchParser extends XMLParser {
  parse(arch) {
    const xmlDoc = this.parseXML(arch);
    const letterId = xmlDoc.getAttribute("letter_id");
    const rejectBy = xmlDoc.getAttribute("reject_by");
    const rejectionReason = xmlDoc.getAttribute("rejection_reason");
    return {
      letterId,
      rejectBy,
      rejectionReason,
    };
  }
}
