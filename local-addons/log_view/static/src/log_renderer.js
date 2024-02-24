/** @odoo-module */
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
var groupBy = function (xs, key) {
  return xs.reduce(function (rv, x) {
    (rv[x[key]] = rv[x[key]] || []).push(x);
    return rv;
  }, {});
};

export class LogRenderer extends Component {
  setup() {
    this.orm = useService("orm");
    this.letters = this.props.letter
      .map((letter) => {
        letter.date = this.formatDate(letter.create_date);
        letter.reject_by = this.formatUser(letter.reject_by);
        letter.letter_id = this.formatId(letter.letter_id);
        letter.time = new Date(
          letter.create_date + " GMT+0000"
        ).toLocaleString();
        // letter.time = letter.create_date.split(" ")[1];
        return letter;
      })
      .sort((a, b) => new Date(b.create_date) - new Date(a.create_date));

    this.letterGroups = groupBy(this.letters, "date");
    this.entries = Object.entries(this.letterGroups);
  }
  formatId(id) {
    if (Array.isArray(id)) {
      return id[1];
    }

    return id;
  }

  formatDate(date) {
    return new Date(date).toLocaleDateString("vi");
  }

  formatUser(user) {
    if (Array.isArray(user)) {
      const mark = user[1].split("-");
      return mark.length > 1 ? mark[1].trim() : mark[0].trim();
    }

    return user;
  }
}

LogRenderer.template = "log_view.LogRenderer";
