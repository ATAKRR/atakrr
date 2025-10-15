# ATAKRR: ATAK Radio Reconnaissance

Please submit PRs or open issues to discuss features. Contact me at atakrr (a@t) ethertech.org to discuss.  

We already have AI/ML, FPGA, and ATAK coders, (Jeffrey Zurita, Jigish Shukla, RIIS, and Adeptus Cyber Solutions) but we are still looking for a high-level architect using python *and* a PCB designer for when we eventually go to the edge.  We'd love to work with you!  

This is currently in proposal stage, I have a proposal for HR001125S0002 that will be submitted at the end of 10/2025.  We're looking for collaborators and funding!

## Overview

ATAKRR is an open-source research and development platform for **passive spectrum monitoring**, **automatic modulation classification (AMC)**, and **RF fingerprinting**, designed to integrate directly with [ATAK (Android Team Awareness Kit)](https://tak.gov/).  

The goal: real-time, shared electromagnetic situational awareness for field teams.  

We're seeking funding grants from DARPA (already submitted) and other military programs and also looking for collaborators and/or businesses who would be interested in developing this.  We're looking for an ATAK and Android programmer, contact at atakrr a@t ethertech.org

You can [find more information on our notion page.](https://bush-whale-713.notion.site/ATAKRR-ATAK-Radio-Reconaissance-1d1969c50c718012a578c902ec7ea564)

---

## Features

- **Passive wideband spectrum monitoring** (1 MHz – 6 GHz with HackRF)
- **Deep learning–based signal classification** (CNN, RNN, Transformer, DBN, GNN)
- **RF fingerprinting** for device-level identification
- **Geolocation**  
  ‣ Triangulation/trilateration with synchronized SDRs  
  ‣ Single-device “fox hunting” direction finding  
- **ATAK integration**  
  ‣ CoT overlays of transmitters and devices  
  ‣ Heatmaps, markers, and device tracking  
- **Dataset tools** for training, augmentation, and few-shot learning

---

## Why ATAKRR?

We are surrounded by signals in the RF domain — a slice of the [electromagnetic (EM) spectrum](https://en.wikipedia.org/wiki/Electromagnetic_spectrum). Humans can only see visible light and hear acoustic waves, but the rest of the EM spectrum is around us all the time.  They are  a portion of what's called [the Electromagnetic (EM) Spectrum](https://en.wikipedia.org/wiki/Electromagnetic_spectrum), which goes from radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, and gamma rays.  We can only see visible light (and hear sound waves, but those are acoustic, not EM) but the entire spectrum is around us all the time.  What we're talking about is making radio waves and microwaves "visible" to us, not just in the sense of "we can see them like colors", but we can understand them like images.

ATAKRR makes these invisible signals “visible” and interpretable:

- “Oh, this is WiFi traffic.”
- “That’s a voice transmission.”
- “This is a jammer.”
- “This Bluetooth device matches a known fingerprint.”

And just like each orange or each person is unique, **each transmitter has unique device fingerprints**. ATAKRR enables you to determine the device type, encoding (“language”), frequency (“color”), and — when possible — the location of each transmitter.

What you'll get is a map, an overlay on your ATAK device with all of the transmitters and their locations, as well as unique device fingerprints when available.  You can see where they are, what they're doing, and in some cases who they're talking to.  You can track the movement of devices over time.  You can track a particular device, see the movement pattern of multiple devices, see the interrelationships of the devices (who they're connected to, when available).  You can track people by their phones and bluetooth devices.  You can find out when people gather.  You can "see" an entire world that was previously hidden to you.

---

## How Does ATAKRR Work?

### Hardware/Signal Collection Layer
- **HackRF** provides a tunable view of the spectrum from 1 MHz to 6 GHz at 20 MSps (≈20 MHz bandwidth).  
- The device scans the spectrum in increments, yielding raw RF data.  
- Other radios (with FPGA/ASIC codecs) can be used to capture protocol-specific details (e.g., WiFi, Bluetooth MACs).  
- For geolocation, multiple synchronized HackRFs feed data to a shared compute node (“The Mothership”).

### Signal Processing/AI Layer
- **Sweep + waterfall** views using `hackrf_sweep`-style scanning.  
- **Signal decoding and feature extraction** via FPGA/ASIC radios when available.  
- **Automatic Modulation Classification (AMC)** using deep learning (CNN, RNN, Transformer, etc.).  
- **RF fingerprinting** for unique device identification.  
- **Low-SNR support** with wavelet/CWT representations and attention models.

### Visualization Layer
- ATAK plugin displays overlays:  
  ‣ Transmitter positions and movement trails  
  ‣ Unique device fingerprints when available  
  ‣ Interrelationships between devices (connections, clusters)  
- Cursor-on-Target (CoT) markers map signals into the ATAK ecosystem for team-shared awareness.

### ATAK Plugin Layer
‣ Visualization overlays in ATAK (heatmaps, signal IDs, threat markers).
‣ Integration with TAK server for team-shared spectrum awareness.
‣ Potential hooks into FoG/BAMMO/PEWPEW modules.

### Dataset + Training Tools
‣ Scripts for recording, preprocessing, and formatting datasets (RadioML, GNU Radio captures).
‣ Data augmentation for multipath, fading, low-SNR.
‣ Meta-learning few-shot classification (for field-captured rare emitters).


ATAKRR consists of a number of different modules/applications/plugins that work together to create a hyperspectral, semantic-rich awareness of your environment.  The most important hurdle at this time is the hardware, which can be varying.  For the RF spectrum, we start with the HackRF, which can receive from 1MHz-6GHz at 20MSps ([20MHz of bandwidth](https://ham.stackexchange.com/questions/18077/how-is-the-hackrf-able-to-achieve-20mhz-of-bandwidth-with-an-adc-that-only-allow), as it has an IQ ADC, with two samples at 90' phase to each other, allowing the full signal to be sampled at that rate).  

This gives you a view of the environment, scanned in 20MHz/s increments, so it sort of pans across the spectrum.  This shows you the raw values at those frequencies, and therotically allows you to receive (and transmit) any "language" or encoding, that uses a bandwidth of less than 20MHz (because otherwise it can only see a part of its signal).  

When receiving FHSS (Frequency-Hopping Spread Spectrum) or other frequency hopping technologies, it needs to sample the entire range of the frequencies, instantaneously, or guess at the sequence of the hopping.  There are other limitations, but these are the main ones.  For this reason, we also use other hardware that natively communicates using the language that's being used, once/when it's known (by scanning).

We then use radios with hardware or, typically FPGA/ASIC software-coded codecs to gather additional information.  For instance, when using WiFi/Bluetooth, we gather the MAC addresses, frequencies and the signal strength.  This allows us to map the location of the transmitters at the time of scan using CoT (Cursor on Target) mapping on ATAK (the Android [Tactical Assault/Team Awareness] Kit).  We can then correlate the frequencies found using the HackRF with the MAC addresses, giving us a more complete picture.

This gives you a generalized location of the devices, in that anything "seen" is within "transmitting distance" of the receiver.  But what if you want more precise location?  What if you need to find the transmitter?  Then we can use triangulation/trilaterization or another single-device "fox hunting" solution we're working on to geolocate or estimate the direction of the transmitter in the respective cases.  We can do this, provided we have at least 3 synchronized HackRF devices.  By taking the measurements and transmitting them to a shared FoG computing node ("The Mothership") we can then do some math and get the precise location of any transmitters, down to a couple m resolution, typically.

---

## What Does This Provide?

- A **map overlay** on ATAK with all detected transmitters.  
- Tracking of device movement over time.  
- Correlation of frequencies with MACs or identifiers.  
- Ability to infer gatherings, relationships, or anomalies from RF activity.  
- Practical situational awareness in environments otherwise invisible.

---

## Repository Structure
/ATAKRR
/docs -> Whitepapers, design docs
/atak_plugin -> Android ATAK plugin (Java/Kotlin)
/rf_modules
/sweep -> HackRF/rtl-sdr sweep tools
/amc -> CNN/RNN/Transformer classifiers
/fingerprint -> RF fingerprinting pipeline
/datasets
/preprocessing
/augmentation
/examples
notebook_rf_classification.ipynb
atak_plugin_demo.mp4

LICENSE -> BSD 2-Clause (or dual-license)
README.md -> This document


---

## Roadmap

**v0.1**  
- Basic HackRF/rtl-sdr sweep module  
- ATAK plugin skeleton (heatmap overlay)  

**v0.2**  
- Integrate AMC module with CNN baseline  
- Dataset preprocessing + augmentation scripts  

**v0.3**  
- Add RF fingerprinting engine  
- Support for multi-device triangulation  

**Future**  
- Transformer/GNN AMC models  
- Few-shot meta-learning for rare emitters  
- FoG/BAMMO/PEWPEW integration hooks  

---

## Contributing

Contributions are welcome! Ideas include:  
- New classifiers or signal representations  
- Support for additional SDR hardware  
- Improvements to the ATAK plugin UI  
- Dataset sharing and augmentation scripts  

Please submit PRs or open issues to discuss features.  Contact me at **atakrr (a@t) ethertech.org**

---

## License

ATAKRR is released under the **BSD 2-Clause License**.  
Core repo is open, while commercial licensing for advanced modules remains possible.

---
