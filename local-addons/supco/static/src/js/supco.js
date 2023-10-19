odoo.define('supco.notification_and_redirect', function(require) {
    "use strict";

    var core = require('web.core');
    var { registry } = require('web.core');
    var { ActionService } = require('web.action_service');

    // We'll create a new action effect to handle our custom action.
    function showNotificationAndRedirect(env, action) {
        if (action.tag === 'show_notification_and_redirect') {
            env.services.notification.add(action.params.message, {
                type: 'info',
                sticky: false,
            });
            return env.services.action.doAction({
                type: 'ir.actions.act_window',
                view_mode: 'list,form',
                views: [[false, 'list'], [false, 'form']],
                res_model: 'supreme.court.letter',  // Updated model's name
            });
        }
    }

    // Add the effect to the registry
    registry.category("action_effect").add("show_notification_and_redirect", showNotificationAndRedirect);

    return {};
});
