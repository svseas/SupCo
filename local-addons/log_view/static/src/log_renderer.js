/** @odoo-module */
import { Component } from "@odoo/owl";

var groupBy = function (xs, key) {
  return xs.reduce(function (rv, x) {
    (rv[x[key]] = rv[x[key]] || []).push(x);
    return rv;
  }, {});
};

export class LogRenderer extends Component {
  setup() {
    this.letters = this.props.letter.map((letter) => {
      letter.create_date = this.formatDate(letter.create_date);
      letter.reject_by = this.formatUser(letter.reject_by);
      letter.id = this.formatId(letter.letter_id);

      return letter;
    });
    this.letterGroups = groupBy(this.letters, "create_date");
    this.entries = Object.entries(this.letterGroups);
    console.log(this.entries);
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
