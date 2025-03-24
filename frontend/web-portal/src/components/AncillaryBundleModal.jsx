/**
 * AncillaryBundleModal.jsx
 * 
 * Modal dialog for configuring or viewing details of an ancillary bundle offer.
 * Displays bundle details and allows adjustments if needed.
 */

import React from 'react';
import PropTypes from 'prop-types';

const AncillaryBundleModal = ({ bundle, onClose }) => {
  if (!bundle) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>{bundle.bundle_type}</h2>
        <ul>
          {bundle.items.map((item, index) => (
            <li key={index}>
              {item.name}: ${item.price}
            </li>
          ))}
        </ul>
        <p>Total Price: ${bundle.total_price}</p>
        <p>Discount: {bundle.discount * 100}%</p>
        <p>Discounted Price: ${bundle.discounted_price}</p>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
};

AncillaryBundleModal.propTypes = {
  bundle: PropTypes.shape({
    bundle_type: PropTypes.string.isRequired,
    items: PropTypes.array.isRequired,
    total_price: PropTypes.number.isRequired,
    discount: PropTypes.number.isRequired,
    discounted_price: PropTypes.number.isRequired,
  }),
  onClose: PropTypes.func.isRequired,
};

export default AncillaryBundleModal;
