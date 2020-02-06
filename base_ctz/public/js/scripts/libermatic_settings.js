export default function libermatic_settings() {
  return {
    refresh: function(frm) {
      frm.add_custom_button('Setup', async function() {
        try {
          await frappe.call({
            method: 'base_ctz.install.setup_defaults',
            freeze: true,
          });
        } finally {
          frm.reload_doc();
        }
      });
    },
  };
}
