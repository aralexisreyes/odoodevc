/** @odoo-module */

import { Component } from "@odoo/owl";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class ProductCombosButton extends Component {

    static template = "custom_pos_screen.ProductCombosButton";

    setup() {
        this.pos = usePos();  // Accede al objeto pos
    }

    async click() {
        // Verifica si existe una orden actual
        const currentOrder = this.pos.get_order();
        
        if (currentOrder) {

            // Añade una nueva orden
            this.pos.add_new_order();
            
            // Reinicia la pantalla de productos
            this.pos.resetProductScreenSearch();
            
            // Muestra la pantalla de productos
            this.pos.showScreen("ProductScreen");

            console.log('Nueva orden creada con éxito');
        } else {
            console.log('No hay una orden activa');
        }
    }

}

// Añade el botón en la ProductScreen
ProductScreen.addControlButton({
    component: ProductCombosButton,
    condition: function () {
        return true;  // Siempre muestra el botón
    },
});
