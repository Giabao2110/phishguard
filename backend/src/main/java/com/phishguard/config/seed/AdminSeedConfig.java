package com.phishguard.config.seed;

import com.phishguard.model.entity.Role;
import com.phishguard.model.entity.User;
import com.phishguard.repository.RoleRepository;
import com.phishguard.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.ApplicationRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.util.StringUtils;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.Locale;

@Configuration
@RequiredArgsConstructor
@Slf4j
public class AdminSeedConfig {

    private final RoleRepository roleRepository;
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    @Value("${app.seed.admin.enabled:false}")
    private boolean seedEnabled;

    @Value("${app.seed.admin.email:}")
    private String adminEmail;

    @Value("${app.seed.admin.password:}")
    private String adminPassword;

    @Value("${app.seed.admin.display-name:Admin}")
    private String adminDisplayName;

    @Value("${app.seed.admin.role:ADMIN}")
    private String adminRole;

    @Bean
    ApplicationRunner seedAdminUser() {
        return args -> {
            if (!seedEnabled) {
                return;
            }

            if (!StringUtils.hasText(adminEmail) || !StringUtils.hasText(adminPassword)) {
                log.warn("Admin seed skipped: set app.seed.admin.email and app.seed.admin.password when app.seed.admin.enabled=true");
                return;
            }

            String normalizedEmail = adminEmail.trim().toLowerCase(Locale.ROOT);
            if (userRepository.existsByEmail(normalizedEmail)) {
                log.info("Admin seed skipped: user already exists for email={}", normalizedEmail);
                return;
            }

            Role role = roleRepository.findByName(adminRole)
                    .orElseGet(() -> {
                        Role newRole = new Role();
                        newRole.setName(adminRole);
                        newRole.setDescription("System role seeded during bootstrap");
                        return roleRepository.save(newRole);
                    });

            User user = new User();
            user.setEmail(normalizedEmail);
            user.setDisplayName(adminDisplayName);
            user.setPasswordHash(passwordEncoder.encode(adminPassword));
            user.setRole(role);
            user.setActive(true);
            userRepository.save(user);

            log.info("Admin seed completed for email={}", normalizedEmail);
        };
    }
}
