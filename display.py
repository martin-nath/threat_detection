def display_assessment(assessment):

    print("\nAssessment")

    print(f"Priority   : {assessment['priority']}")
    print(f"Score      : {assessment['score']}")

    if assessment["categories"]:
        print(
            f"Categories : {', '.join(assessment['categories'])}"
        )
    else:
        print("Categories : None")

    if assessment["events"]:

        print("Events:")

        for event in assessment["events"]:

            print(
                f"  - {event['label']} "
                f"({event['confidence']:.3f})"
            )

    else:

        print("Events     : None")

def display_decision(decision):

    print("\nDecision")

    if (
        not decision["save_evidence"]
        and
        not decision["send_alert"]
    ):

        print("Action : No action required.")
        return

    if decision["save_evidence"]:

        print("✓ Save Evidence")

    if decision["send_alert"]:

        print("✓ Send Alert")