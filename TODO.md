# TODO #

## Important ##
  * <strike>Figure out best way to mark messages read.</strike>
    * Solution: leave it up to each app to keep a Log - _do not_ rely on backend. But, provide pre-made Log model in samosa.util.models
    * Comment: this results in a lot of boilerplate code in each response method of each app - cluttery and hard to maintain for larger apps.
      * If the messages aren't logged (and thus marked as read) until somewhere in the response, messages that cause exceptions prior to the logging will keep cropping up, like that one unmatched black sock in your drawer. Robust response writing is as important as anything else, but we can make that job easier.
    * Alternatives:
      * Log each message that passes a test, in the core controller - why not?
      * provide a hook for apps to handle response-invariant bookkeeping/behavior (called when any test is passed, or when any response method returns).
  * Define use of models
    * Using MongoEngine now, but still have to figure out how to keep different apps from screwing with each other's documents and/or how to be connected to multiple MongoDBs at the same time.
    * Assuming messages are handled on a single thread(`*`), what would happen if ME.connect(appname) were called before each test or response? (in a pre-test hook, for example)
      * (`*`) note that weird concurrency things do happen when a check is forced from the command line - the checker loop is operating on a separate thread. "JSON Errors" result when the two checks overlap.
  * More high-volume testing is needed (before the Weekender?) - during the Hidden Grove test, some replies weren't sent (or the messages not processed?) for tens of minutes after the messages were received.
    * This may be a result of different carriers' message-relay policies, or throttling on GV's part.
    * I want to experiment with a (1s?) delay in send-to-all loops to see if we can beat the hypothetical throttling.

## Less Important ##
  * Add email as another backend
    * How to reconcile 160 char limit??
  * What really are required/optional attrs of Message objects?