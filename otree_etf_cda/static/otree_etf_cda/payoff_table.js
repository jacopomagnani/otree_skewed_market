import { html, PolymerElement } from '/static/otree-redwood/node_modules/@polymer/polymer/polymer-element.js';
import '/static/otree-redwood/node_modules/@polymer/polymer/lib/elements/dom-repeat.js';

// calc greatest common denominator of two numbers
function gcd(a, b) {
    while (a % b > 0) {
        const tmp = a % b;
        a = b;
        b = tmp;
    }
    return b;
}

class PayoffTable extends PolymerElement {

    static get properties() {
        return {
            assetStructure: Object,
            stateProbabilities: Object,
            assetNames: Array,
            stateNames: {
                type: Array,
                computed: '_computeStateNames(stateProbabilities)',
            },
        };
    }

    static get template() {
        return html`
            <style>
                .container {
                    padding: 10px;
                }
                .table {
                    text-align: center;
                    display: flex;
                }
                .table > div {
                    display: flex;
                    flex-direction: column;
                }
                .table > :first-child {
                    text-align: center;
                }
                .table > div > :first-child{
                }
                .table span {
                    padding: 0 0.5em 0 0.5em;
                    height: 1.5em;
                    border: 1px solid black;
                }
                .mytable {
                    display: flex;
                    flex-direction: row;
                }


            </style>

            <div class="mytable">
                <div class="container">
                    <span>Actif X</span>
                    <div class="table">
                        <div>
                            <span>Gain</span>
                            <span>Chance</span>
                        </div>
                        <div>
                            <span>[[_getPayoff("X", 0, assetStructure)]]</span>
                            <span>[[_getProbability("X", 0, assetStructure)]]%</span>
                        </div>
                        <div>
                            <span>[[_getPayoff("X", 1, assetStructure)]]</span>
                            <span>[[_getProbability("X", 1, assetStructure)]]%</span>
                        </div>
                    </div>
                </div>

                <div class="container">
                    <span>Actif Y</span>
                    <div class="table">
                        <div>
                            <span>Gain</span>
                            <span>Chance</span>
                        </div>
                        <div>
                            <span>[[_getPayoff("Y", 0, assetStructure)]]</span>
                            <span>[[_getProbability("Y", 0, assetStructure)]]%</span>
                        </div>
                        <div>
                            <span>[[_getPayoff("Y", 1, assetStructure)]]</span>
                            <span>[[_getProbability("Y", 1, assetStructure)]]%</span>
                        </div>
                    </div>
                </div>

                <div class="container">
                    <span>Actif Z</span>
                    <div class="table">
                        <div>
                            <span>Gain</span>
                            <span>Chance</span>
                        </div>
                        <div>
                            <span>[[_getPayoff("Z", 0, assetStructure)]]</span>
                            <span>[[_getProbability("Z", 0, assetStructure)]]%</span>
                        </div>
                    </div>
                </div>
            </div>




            
        `;
    }

    _computeStateNames(stateProbabilities) {
        return Object.keys(stateProbabilities);
    }

    _getPayoff(assetName, state, assetStructure) {
        if (!assetStructure)
            return;
        const structure = assetStructure[assetName];
        if (structure.is_etf) {
            let payoff = 0;
            for (const [componentAsset, weight] of Object.entries(structure.etf_weights)) {
                payoff += assetStructure[componentAsset].payoffs[state] * weight;
            }
            return payoff;
        }
        else {
            return assetStructure[assetName].payoffs[state];
        }
    }

        _getProbability(assetName, state, assetStructure) {
        if (!assetStructure)
            return;
        const structure = assetStructure[assetName];
        if (structure.is_etf) {
            let payoff = 0;
            for (const [componentAsset, weight] of Object.entries(structure.etf_weights)) {
                payoff += assetStructure[componentAsset].payoffs[state] * weight;
            }
            return payoff;
        }
        else {
            return assetStructure[assetName].probabilities[state];
        }
    }

}

window.customElements.define('payoff-table', PayoffTable);