# Release Checklist (iOS App Store), generic template

Copy this file into each product's pack. Product-specific facts go in release_facts.md, not here.

Maintained by the Release Manager. Status: Todo / In progress / Done / Blocked / Unverified. Verify requirements against Apple's current documentation before relying on them.

## 0. Facts to collect from the owner (record the answers in release_facts.md)
- [ ] App status: coded and running, or design only? Tech stack and who builds and signs the app
- [ ] Apple Developer account: individual or organisation, who owns it
- [ ] Final app name, bundle ID, support email, website and privacy policy URL
- [ ] Login method: none, email, Sign in with Apple, other (account deletion needed if accounts exist)
- [ ] Third-party services: AI provider, analytics, crash reporting, payments, ads
- [ ] Data collected and what is sent to third parties
- [ ] Minimum age decision
- [ ] Final prices, trial length and regions (if paid)

## 1. Accounts and setup
- [ ] Apple Developer Program membership active
- [ ] App record created in App Store Connect; name availability checked
- [ ] Bundle ID and capabilities (HealthKit, Push, In-App Purchase, Sign in with Apple if used)
- [ ] Signing and provisioning ready
- [ ] Agreements, tax and banking set up for paid apps and subscriptions (owner only)

## 2. Product readiness
- [ ] Required flows exist: sign-in (if accounts), settings, account deletion (if accounts), subscription management (if paid), permission handling, empty and error states
- [ ] Permissions requested in context with clear purpose strings
- [ ] Any AI feature: user consent and disclosure for sending data to the provider
- [ ] Copy reviewed for claims that need substantiation (medical, financial, performance)
- [ ] Placeholder names, wordmarks and splash updated to the final name
- [ ] Fonts, icons and images licensed
- [ ] Category-specific checks done (health, finance, kids, user content), see release_facts.md

## 3. Build and TestFlight
- [ ] Built with the currently required Xcode and SDK (verify)
- [ ] Privacy manifest and required-reason API declarations; third-party SDK manifests
- [ ] Internal TestFlight group tested
- [ ] External TestFlight (beta review) if needed
- [ ] Critical flows tested (list them in release_facts.md): first run, purchase and restore if paid, core feature, offline, permission denied

## 4. Store listing
- [ ] Name, subtitle, promotional text, description, keywords
- [ ] Category, age rating questionnaire, copyright
- [ ] Support URL, marketing URL, privacy policy URL
- [ ] Icon 1024 px
- [ ] Screenshots for each required device size; captions; order
- [ ] What's new text; localisation plan (English first)

## 5. Privacy and legal
- [ ] Privacy policy published and linked in app and listing
- [ ] Terms of use / EULA and subscription terms
- [ ] App Privacy answers completed (collection, linking, tracking)
- [ ] Account deletion available in app if accounts exist
- [ ] Lawyer review of privacy policy and terms

## 6. Subscriptions
- [ ] Subscription group, products, prices by region, free trial
- [ ] Paywall shows price, period, renewal terms, trial terms; Restore; Terms and Privacy links
- [ ] Review screenshot for each IAP
- [ ] Cancellation and management information

## 7. Submission
- [ ] App Review information: contact, demo access, notes (AI, health data, subscriptions)
- [ ] Export compliance (encryption) answered
- [ ] Release option chosen (manual, automatic, phased)
- [ ] Submitted by owner; status tracked

## 8. After submission
- [ ] Rejection response plan ready
- [ ] Monitoring: crashes, reviews, subscription metrics
- [ ] Next version plan linked to the roadmap
