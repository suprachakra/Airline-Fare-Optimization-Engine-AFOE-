// AppDelegate.swift
// Stub example for iOS entry point.
// In a full native iOS app, this file sets up the application and integrates with the React Native bridge.

import UIKit
import React

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

  var window: UIWindow?

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let bridge = RCTBridge(delegate: self, launchOptions: launchOptions)
    let rootView = RCTRootView(bridge: bridge!, moduleName: "AirlineFareOptimizationApp", initialProperties: nil)
    rootView.backgroundColor = UIColor.white

    self.window = UIWindow(frame: UIScreen.main.bounds)
    let rootViewController = UIViewController()
    rootViewController.view = rootView
    self.window?.rootViewController = rootViewController
    self.window?.makeKeyAndVisible()
    return true
  }
}

// MARK: - RCTBridgeDelegate
extension AppDelegate: RCTBridgeDelegate {
  func sourceURL(for bridge: RCTBridge!) -> URL! {
#if DEBUG
    return RCTBundleURLProvider.sharedSettings().jsBundleURL(forBundleRoot: "index", fallbackResource: nil)
#else
    return Bundle.main.url(forResource: "main", withExtension: "jsbundle")
#endif
  }
}
