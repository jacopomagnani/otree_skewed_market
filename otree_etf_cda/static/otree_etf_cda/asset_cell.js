import { html, PolymerElement } from '/static/otree-redwood/node_modules/@polymer/polymer/polymer-element.js';
import '/static/otree-redwood/src/otree-constants/otree-constants.js';
import '/static/otree_markets/order_list.js';
import '/static/otree_markets/trade_list.js';

import './currency_scaler.js';

class AssetCell extends PolymerElement {

    static get properties() {
        return {
            assetName: String,
            bids: Array,
            asks: Array,
            trades: Array,
        };
    }

    static get template() {
        return html`
            <style>
                * {
                    box-sizing: border-box;
                }
                .main-container {
                    height: 100%;
                    display: flex;
                    flex-direction: column;
                    border: 1px solid black;
                }
                h3, h5 {
                    margin: 0;
                    text-align: center;
                }
                order-list, trade-list {
                    border: 1px solid black;
                }

                .list {
                    flex: 1;
                    display: flex;
                    padding: 0 2px 0 2px;
                    min-height: 0;
                }
                .list > div {
                    display: flex;
                    flex-direction: column;
                    height: 100%;
                    flex: 1;
                    margin: 0 2px 0 2px;
                }
                .list > div > :last-child {
                    flex: 1;
                    min-height: 0;
                }

                .buttons > div {
                    display: flex;
                    align-items: center;
                    width: 33%;
                    height: 100%;
                    padding: 5px;
                }
                .buttons > div:first-child {
                    float: left;
                }
                .buttons > div:last-child {
                    float: right;
                }
                .buttons input {
                    flex: 1;
                    min-width: 40px;
                }
                .buttons > div > * {
                    margin: 5px;
                }
            </style>

            <otree-constants
                id="constants"
            ></otree-constants>
            <currency-scaler
                id="currency_scaler"
            ></currency-scaler>

            <div class="main-container">
                <h3>Actif [[assetName]]</h3>
                <div class="list">
                    <div>
                        <h5>Offres d’achat</h5>
                        <order-list
                            asset-name="[[assetName]]"
                            orders="[[bids]]"
                            display-format="[[orderDisplayFormat]]"
                        ></order-list>
                    </div>
                    <div>
                        <h5>Transactions</h5>
                        <trade-list
                            asset-name="[[assetName]]"
                            trades="[[trades]]"
                            display-format="[[tradeDisplayFormat]]"
                        ></trade-list>
                    </div>
                    <div>
                        <h5>Offres de vente</h5>
                        <order-list
                            asset-name="[[assetName]]"
                            orders="[[asks]]"
                            display-format="[[orderDisplayFormat]]"
                        ></order-list>
                    </div>
                </div>
                <div class="buttons">
                    <div>

                        <input id="bid_price" type="number" min="0" step="[[price_step]]">
                        <button type="button" on-click="_enter_order" value="bid">Faire une offre d’achat</button>
                    </div>
                    <div>

                        <input id="ask_price" type="number" min="0" step="[[price_step]]">
                        <button type="button" on-click="_enter_order" value="ask">Faire une offre de vente</button>
                    </div>
                </div>
            </div>
        `;
    }

    ready() {
        super.ready();
        this.pcode = this.$.constants.participantCode;
        this.price_step = 1 / this.$.currency_scaler.factor;

        this.orderDisplayFormat = order => {
            const price = this.$.currency_scaler.toHumanReadable(order.price);
            return price;
        };
        this.tradeDisplayFormat = (making_order, taking_order) => {
            // booleans. true if this player bought/sold in this trade
            const bought = (making_order.pcode == this.pcode &&  making_order.is_bid) || (taking_order.pcode == this.pcode &&  taking_order.is_bid);
            const sold   = (making_order.pcode == this.pcode && !making_order.is_bid) || (taking_order.pcode == this.pcode && !taking_order.is_bid);

            // buy_sell_indicator is 'B' if this player bought, 'S' if they sold, 'BS' if they did both
            // and empty string otherwise
            let buy_sell_indicator = '';
            if (bought && sold) buy_sell_indicator = ' BS';
            else if (bought)    buy_sell_indicator = ' A';
            else if (sold)      buy_sell_indicator = ' V';

            const price = this.$.currency_scaler.toHumanReadable(making_order.price);

            return `${price}${buy_sell_indicator}`
        };
    }

    _enter_order(event) {
        const is_bid = (event.target.value == 'bid');
        const price = parseFloat(this.$[is_bid ? 'bid_price' : 'ask_price'].value);
        const price_scaled = this.$.currency_scaler.fromHumanReadable(price);
        const order = {
            price: price_scaled,
            // unit volume
            volume: 1,
            is_bid: is_bid,
            asset_name: this.assetName,
        }
        this.dispatchEvent(new CustomEvent('order-entered', {detail: order}));
    }

}

window.customElements.define('asset-cell', AssetCell);
