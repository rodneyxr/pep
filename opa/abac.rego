package abac

default allow = false

hasClearance(user, document) {
	user.clearance >= document.clearance
}

# document.attributes must be a subset of user.attributes
hasAllAttributes(user, document) {
	count({attr | attr := document.attributes[_]; attr == user.attributes[_]}) == count(document.attributes)
}

allow {
	hasClearance(input.user, input.document)
	hasAllAttributes(input.user, input.document)
}
