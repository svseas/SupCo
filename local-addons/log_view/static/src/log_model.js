/** @odoo-module */
import { KeepLast } from "@web/core/utils/concurrency";

export class LogModel {
  constructor(orm, resModel, archInfo, domain) {
    this.orm = orm;
    this.resModel = resModel;
    const { letterId, rejectBy, rejectionReason } = archInfo;
    this.letterId = letterId;
    this.rejectBy = rejectBy;
    this.rejectionReason = rejectionReason;
    this.domain = domain;
    this.keepLast = new KeepLast();
  }

  async load() {
    const { records } = await this.keepLast.add(
      this.orm.webSearchRead(this.resModel, this.domain, [
        "letter_id",
        this.letterId,
        "reject_by",
        this.rejectionReason,
        "create_date"
      ])
    );

    this.letter = records;
  }
}
