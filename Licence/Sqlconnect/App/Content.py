# <div id="licenseStatusFields" style="display: none;">
#   <div class="mb-3 row">
#       <label for="{{ license_status_form.nvarmacaddress.id_for_label }}" class="col-sm-4 col-form-label">Mac Address</label>
#       <div class="col-sm-8">
#           {{ license_status_form.nvarmacaddress }}
#       </div>
#   </div>
#   <div class="mb-3 row">
#       <label for="{{ license_status_form.dtstartdate.id_for_label }}" class="col-sm-4 col-form-label">Start Date</label>
#       <div class="col-sm-8">
#           {{ license_status_form.dtstartdate }}
#       </div>
#   </div>
#   <div class="mb-3 row">
#       <label for="{{ license_status_form.dtenddate.id_for_label }}" class="col-sm-4 col-form-label">End Date</label>
#       <div class="col-sm-8">
#           {{ license_status_form.dtenddate }}
#       </div>
#   </div>
# </div>


# licence_form.html


# <!--{% extends 'base.html' %}-->
# <!--{% block title %}License Form{% endblock %}-->
# <!--{% block content %}-->
# <!--<div class="container mt-5">-->
# <!--    <div class="row justify-content-center">-->
# <!--        <div class="col-md-8">-->
# <!--            <div class="card">-->
# <!--                <div class="card-header bg-primary text-white">-->
# <!--                    <h2 class="mb-0">Add a New License</h2>-->
# <!--                </div>-->
# <!--                <div class="card-body">-->
# <!--&lt;!&ndash;                    <p>Debug: intclientid = {{ client.intid }}</p>&ndash;&gt;-->
# <!--                    <form method="post" action="{% url 'licence_add' intclientid=client.intid %}" id="licenseForm">-->
# <!--                        {% csrf_token %}-->
# <!--                        <div class="mb-3 row">-->
# <!--                            <label for="{{ client_license_form.intclientid.id_for_label }}" class="col-sm-4 col-form-label">Client ID</label>-->
# <!--                            <div class="col-sm-8">-->
# <!--                                {{ client_license_form.intclientid }}-->
# <!--                            </div>-->
# <!--                        </div>-->
# <!--                        <div class="mb-3 row">-->
# <!--                            <label for="{{ client_license_form.nvarkey.id_for_label }}" class="col-sm-4 col-form-label">License Key</label>-->
# <!--                            <div class="col-sm-4">-->
# <!--                                {{ client_license_form.nvarkey }}-->
# <!--                            </div>-->
# <!--                            <div class="col-sm-4">-->
# <!--                                <button type="button" id="generateKeyBtn" class="btn btn-secondary btn-sm">Generate Key</button>-->
# <!--                            </div>-->
# <!--                        </div>-->
# <!--                        <div class="mb-3 row">-->
# <!--                            <label for="{{ client_license_form.intvalidity.id_for_label }}" class="col-sm-4 col-form-label">Validity (days)</label>-->
# <!--                            <div class="col-sm-8">-->
# <!--                                {{ client_license_form.intvalidity }}-->
# <!--                            </div>-->
# <!--                        </div>-->
# <!--&lt;!&ndash;                        <div class="mb-3 row">&ndash;&gt;-->
# <!--&lt;!&ndash;                            <label for="{{ client_license_form.nvarreference.id_for_label }}" class="col-sm-4 col-form-label">Reference</label>&ndash;&gt;-->
# <!--&lt;!&ndash;                            <div class="col-sm-8">&ndash;&gt;-->
# <!--&lt;!&ndash;                                {{ client_license_form.nvarreference }}&ndash;&gt;-->
# <!--&lt;!&ndash;                            </div>&ndash;&gt;-->
# <!--&lt;!&ndash;                        </div>&ndash;&gt;-->
# <!--                        <div class="mb-3 row">-->
# <!--                            <label for="{{ client_license_form.bitactive.id_for_label }}" class="col-sm-4 col-form-label">Active</label>-->
# <!--                            <div class="col-sm-8">-->
# <!--                                {{ client_license_form.bitactive }}-->
# <!--                            </div>-->
# <!--                        </div>-->
# <!--                        &lt;!&ndash; Add more form fields as needed &ndash;&gt;-->
#
# <!--                        <div class="d-grid gap-2">-->
# <!--                            <button type="submit" class="btn btn-primary">Save</button>-->
# <!--                            <a href="{% url 'licence' client_id=client.intid %}" class="btn btn-secondary">Back</a>-->
# <!--                        </div>-->
# <!--                    </form>-->
# <!--                </div>-->
# <!--            </div>-->
# <!--        </div>-->
# <!--    </div>-->
# <!--</div>-->
#
# <!--<script>-->
# <!--    // Add event listener to toggle the visibility of license status fields-->
# <!--    document.getElementById('id_bitactive').addEventListener('change', function() {-->
# <!--        var licenseStatusFields = document.getElementById('licenseStatusFields');-->
# <!--        if (this.checked) {-->
# <!--            licenseStatusFields.style.display = 'block';-->
# <!--        } else {-->
# <!--            licenseStatusFields.style.display = 'none';-->
# <!--        }-->
# <!--    });-->
#
# <!--    // Add event listener to generate random key-->
# <!--    document.getElementById('generateKeyBtn').addEventListener('click', function() {-->
# <!--        // Customize this function to generate your desired key format-->
# <!--        var randomKey = generateRandomKey();-->
# <!--        document.getElementById('id_nvarkey').value = randomKey;-->
# <!--    });-->
#
# <!--    // Function to generate a random key-->
# <!--    function generateRandomKey() {-->
# <!--        // Customize this function to generate your desired key format-->
# <!--        // For simplicity, we're using a random 10-character alphanumeric key-->
# <!--        var key = Math.random().toString(36).substring(2, 14).toUpperCase();-->
# <!--        return key;-->
# <!--    }-->
#
# <!--</script>-->
#
# <!--{% endblock %}-->

# {% url 'licence' client_id=client_license.intclientid_id %}