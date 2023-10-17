/** @odoo-module */
import { useState, reactive } from "@odoo/owl";
import { ContentContainer } from "../content-container/content-container";

export const contentStore = reactive({
  content: ContentContainer,
  changeContent(component) {
    this.content = component;
  },
});

function useContentStore() {
  return useState(contentStore);
}

export { useContentStore };
