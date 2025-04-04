# Proxy2JMX Converter

It's possible to convert existing Selenium scripts into JMeter JMX file. Keep in mind: only requests will be converted, no assertions or other logic. Also note that it will only capture requests going to publicly available servers, so `localhost` or behind the firewall won't be captured.
For this purpose Taurus uses [BlazeMeter Recorder](https://help.blazemeter.com/docs/guide/recorders-creating-the-proxy-recorder.html) so you need valid token. This service starts proxy for logging requests and build jmx file based on the requests when test is finished. You will need a [BlazeMeter API key configured](BlazemeterReporter/#Personalized-Usage) for this approach to work. Let's see example config:

```yaml
execution:
- executor: selenium
  iterations: 1
  scenario: sel

scenarios:
  sel:
    script: example.java

services:
- module: proxy2jmx
```

As soon as taurus completes its work you'll find JMX files in the artifacts dir with the names `generated.simple.jmx` and `generated.smart.jmx`. SmartJMX is a feature to help with JMX parameterization and is explained in detail in [this article](https://www.blazemeter.com/blog/correlation-in-jmeter).

If you want to change the resulting name of generated JMX files, use the `simple-output` and/or `smart-output` options of Proxy2JMX module like this:

```yaml
services:
- module: proxy2jmx
  simple-output: result.jmx
  smart-output: result-clean.jmx
```

## Proxy Server Auto Setup
Taurus can help you with settings of proxy server for recording purposes. This ability depends on your operating system.

### Linux 
Full support of Chrome and Firefox.

### Microsoft Windows
We provide support of Chrome browser at the moment. For correct work of proxy you have to prepare the right place
for chromedriver (don't place your chromedriver inside Windows directory). We strongly recommend the next way:
1. create directory (e.g. "c:\chromedriver")
2. put chromedriver.exe into created directory and remove all another copies of chromedriver
3. add directory to path:
   1. go to `Control Panel` -> `System and Security` -> `System`
   2. `Advanced system settings` -> `Environment Variables`
   3. in the `System Variables` area locate the `Path` variable, highlight it and click `Edit`
   4. add your path (`c:\chromedriver`) to previous value (and don't forget about path separator `;`)
   5. save changes.
4. don't run Taurus from Admin account or Admin terminal
5. don't hardcode the path to chromedriver.exe in your scripts

Note: As proxy2jmx uses own proxy, it doesn't support top level [proxy option](ConfigSyntax.md#Top-Level-Settings). 

### MacOS
Auto setup in macOS is currently not implemented.
